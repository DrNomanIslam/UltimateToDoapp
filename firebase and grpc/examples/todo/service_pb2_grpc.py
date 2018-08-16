# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class ToDoStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTasks = channel.unary_unary(
        '/todo.ToDo/GetTasks',
        request_serializer=service__pb2.Empty.SerializeToString,
        response_deserializer=service__pb2.Tasks.FromString,
        )
    self.GetTask = channel.unary_unary(
        '/todo.ToDo/GetTask',
        request_serializer=service__pb2.TaskRequest.SerializeToString,
        response_deserializer=service__pb2.Task.FromString,
        )
    self.UpdateTask = channel.unary_unary(
        '/todo.ToDo/UpdateTask',
        request_serializer=service__pb2.Task.SerializeToString,
        response_deserializer=service__pb2.TaskStatus.FromString,
        )
    self.AddTask = channel.unary_unary(
        '/todo.ToDo/AddTask',
        request_serializer=service__pb2.Task.SerializeToString,
        response_deserializer=service__pb2.TaskStatus.FromString,
        )
    self.DeleteTask = channel.unary_unary(
        '/todo.ToDo/DeleteTask',
        request_serializer=service__pb2.TaskRequest.SerializeToString,
        response_deserializer=service__pb2.TaskStatus.FromString,
        )


class ToDoServicer(object):
  """The greeting service definition.
  """

  def GetTasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ToDoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTasks': grpc.unary_unary_rpc_method_handler(
          servicer.GetTasks,
          request_deserializer=service__pb2.Empty.FromString,
          response_serializer=service__pb2.Tasks.SerializeToString,
      ),
      'GetTask': grpc.unary_unary_rpc_method_handler(
          servicer.GetTask,
          request_deserializer=service__pb2.TaskRequest.FromString,
          response_serializer=service__pb2.Task.SerializeToString,
      ),
      'UpdateTask': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTask,
          request_deserializer=service__pb2.Task.FromString,
          response_serializer=service__pb2.TaskStatus.SerializeToString,
      ),
      'AddTask': grpc.unary_unary_rpc_method_handler(
          servicer.AddTask,
          request_deserializer=service__pb2.Task.FromString,
          response_serializer=service__pb2.TaskStatus.SerializeToString,
      ),
      'DeleteTask': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteTask,
          request_deserializer=service__pb2.TaskRequest.FromString,
          response_serializer=service__pb2.TaskStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'todo.ToDo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
