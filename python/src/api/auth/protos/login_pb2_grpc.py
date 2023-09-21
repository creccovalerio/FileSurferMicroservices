# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protos.login_pb2 as login__pb2


class LoginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.doLogin = channel.unary_unary(
                '/auth.Login/doLogin',
                request_serializer=login__pb2.LoginRequest.SerializeToString,
                response_deserializer=login__pb2.LoginReply.FromString,
                )
        self.doRegistration = channel.unary_unary(
                '/auth.Login/doRegistration',
                request_serializer=login__pb2.RegistrationRequest.SerializeToString,
                response_deserializer=login__pb2.RegistrationReply.FromString,
                )
        self.doValidate = channel.unary_unary(
                '/auth.Login/doValidate',
                request_serializer=login__pb2.ValidateRequest.SerializeToString,
                response_deserializer=login__pb2.ValidateReply.FromString,
                )


class LoginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def doLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doRegistration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doValidate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoginServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'doLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.doLogin,
                    request_deserializer=login__pb2.LoginRequest.FromString,
                    response_serializer=login__pb2.LoginReply.SerializeToString,
            ),
            'doRegistration': grpc.unary_unary_rpc_method_handler(
                    servicer.doRegistration,
                    request_deserializer=login__pb2.RegistrationRequest.FromString,
                    response_serializer=login__pb2.RegistrationReply.SerializeToString,
            ),
            'doValidate': grpc.unary_unary_rpc_method_handler(
                    servicer.doValidate,
                    request_deserializer=login__pb2.ValidateRequest.FromString,
                    response_serializer=login__pb2.ValidateReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Login', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Login(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def doLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Login/doLogin',
            login__pb2.LoginRequest.SerializeToString,
            login__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doRegistration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Login/doRegistration',
            login__pb2.RegistrationRequest.SerializeToString,
            login__pb2.RegistrationReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doValidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Login/doValidate',
            login__pb2.ValidateRequest.SerializeToString,
            login__pb2.ValidateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
