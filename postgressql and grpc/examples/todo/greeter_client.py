from __future__ import print_function

import grpc

import service_pb2
import service_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ToDoStub(channel)
        #response = stub.AddTask(service_pb2.Task(task_id='1', description="GRPC",title="GRPC Title",done="True"))
        #response = stub.UpdateTask(service_pb2.Task(task_id='1', description="GRPC",title="GRPC Title",done="True"))
        #response = stub.DeleteTask(service_pb2.TaskRequest(task_id='1'))
        #response = stub.GetTask(service_pb2.TaskRequest(task_id='1'))
        response = stub.GetTasks(service_pb2.Empty())
    print("Greeter client received: " + str(response))


if __name__ == '__main__':
    run()