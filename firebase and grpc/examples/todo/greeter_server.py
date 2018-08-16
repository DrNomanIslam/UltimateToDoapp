from concurrent import futures
import time
from db import DB
import grpc
import json
import service_pb2
import service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ToDo(service_pb2_grpc.ToDoServicer):

    def GetTasks(self, request, context):
        r=[]
        tasks=DB().get_all().val()
        for obj in tasks:
            if obj:
                _, obj = obj.popitem()
                r.append(service_pb2.Task(task_id=obj['id'],description=obj['description'],title=obj['title'],done=obj['done']))
        return service_pb2.Tasks(tasks=r)


    def GetTask(self, request, context):
        obj=DB().get_task(request.task_id).val()
        _, obj = obj.popitem()
        return service_pb2.Task(task_id=obj['id'],description=obj['description'],title=obj['title'],done=obj['done'])

    def UpdateTask(self, request, context):
        DB().update_task(request.task_id,request.description,request.title,request.done)
        return service_pb2.TaskStatus(status="Task Updated Successfully")

    def AddTask(self, request, context):
        DB().addToDo(request.task_id,request.description,request.title,request.done)
        return service_pb2.TaskStatus(status="Task added Successfully")

    def DeleteTask(self, request, context):
        DB().remove_task(request.task_id)
        return service_pb2.TaskStatus(status="Task deleted Successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ToDoServicer_to_server(ToDo(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()