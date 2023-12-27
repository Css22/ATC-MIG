# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import util.sharing as util
import grpc_tool.server_scherduler_pb2 as server__scherduler__pb2


class SchedulerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JobState = channel.unary_unary(
                '/SchedulerService/JobState',
                request_serializer=server__scherduler__pb2.JobStateMessage.SerializeToString,
                response_deserializer=server__scherduler__pb2.ReplyResult.FromString,
                )
        self.Predictor = channel.unary_unary(
                '/SchedulerService/Predictor',
                request_serializer=server__scherduler__pb2.JobCombine.SerializeToString,
                response_deserializer=server__scherduler__pb2.ReplyPrediction.FromString,
                )
        self.Load = channel.unary_unary(
                '/SchedulerService/Load',
                request_serializer=server__scherduler__pb2.LoadInformation.SerializeToString,
                response_deserializer=server__scherduler__pb2.ReplyResult.FromString,
                )
        self.Regist = channel.unary_unary(
                '/SchedulerService/Regist',
                request_serializer=server__scherduler__pb2.NodeInformation.SerializeToString,
                response_deserializer=server__scherduler__pb2.ReplyResult.FromString,
                )


class SchedulerServiceServicer(object):

    def __init__(self, Scheduler):
        self.Scheduler = Scheduler

    def JobState(self, request, context):
        print(request.type, request.JobID)
        reply = server__scherduler__pb2.ReplyResult(response = 'successful!')
        return  reply 

    def Predictor(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Load(self, request, context):
        self.Scheduler.update_load(request)
        reply = server__scherduler__pb2.ReplyResult(response = 'successful!')
 
        return  reply 

    def Regist(self, request, context):

        self.Scheduler.add_worker(request)
        reply = server__scherduler__pb2.ReplyResult(response = 'successful!')
        return  reply 


def add_SchedulerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JobState': grpc.unary_unary_rpc_method_handler(
                    servicer.JobState,
                    request_deserializer=server__scherduler__pb2.JobStateMessage.FromString,
                    response_serializer=server__scherduler__pb2.ReplyResult.SerializeToString,
            ),
            'Predictor': grpc.unary_unary_rpc_method_handler(
                    servicer.Predictor,
                    request_deserializer=server__scherduler__pb2.JobCombine.FromString,
                    response_serializer=server__scherduler__pb2.ReplyPrediction.SerializeToString,
            ),
            'Load': grpc.unary_unary_rpc_method_handler(
                    servicer.Load,
                    request_deserializer=server__scherduler__pb2.LoadInformation.FromString,
                    response_serializer=server__scherduler__pb2.ReplyResult.SerializeToString,
            ),
            'Regist': grpc.unary_unary_rpc_method_handler(
                    servicer.Regist,
                    request_deserializer=server__scherduler__pb2.NodeInformation.FromString,
                    response_serializer=server__scherduler__pb2.ReplyResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SchedulerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SchedulerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JobState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SchedulerService/JobState',
            server__scherduler__pb2.JobStateMessage.SerializeToString,
            server__scherduler__pb2.ReplyResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Predictor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SchedulerService/Predictor',
            server__scherduler__pb2.JobCombine.SerializeToString,
            server__scherduler__pb2.ReplyPrediction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Load(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SchedulerService/Load',
            server__scherduler__pb2.LoadInformation.SerializeToString,
            server__scherduler__pb2.ReplyResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Regist(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SchedulerService/Regist',
            server__scherduler__pb2.NodeInformation.SerializeToString,
            server__scherduler__pb2.ReplyResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class WorkerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AccpetJob = channel.unary_unary(
                '/WorkerService/AccpetJob',
                request_serializer=server__scherduler__pb2.JobInformation.SerializeToString,
                response_deserializer=server__scherduler__pb2.ReplyResult.FromString,
                )


class WorkerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""
    def __init__(self, worker):
        self.worker = worker

    def AccpetJob(self, request, context):
        job = util.get_job(request.JobID)
        if self.worker.node_schedule(job, request.GPU_ID):
            reply = server__scherduler__pb2.ReplyResult(response = 'successful')
            return reply
        else:
            reply = server__scherduler__pb2.ReplyResult(response = 'Lose')
            return reply



def add_WorkerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AccpetJob': grpc.unary_unary_rpc_method_handler(
                    servicer.AccpetJob,
                    request_deserializer=server__scherduler__pb2.JobInformation.FromString,
                    response_serializer=server__scherduler__pb2.ReplyResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'WorkerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AccpetJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WorkerService/AccpetJob',
            server__scherduler__pb2.JobInformation.SerializeToString,
            server__scherduler__pb2.ReplyResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
