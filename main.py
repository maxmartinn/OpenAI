from OpenAI import OpenAI
from ConfigService import ConfigService
from protos.gen import OpenAIService_pb2_grpc, OpenAIService_pb2
import grpc
from concurrent import futures

class Application(OpenAIService_pb2_grpc.OpenAIServiceServicer):
    def __init__(self):
        self.config_service = ConfigService()
        self.openai = OpenAI(self.config_service)
        
    def BasicChat(self, request, context):
        model = "gpt-3.5-turbo"
        prompt, system_message = request.prompt, request.system_message
        response = self.openai._client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        response_text = response.choices[0].message.content
        print(f"OpenAI Response: {response_text}")
        return OpenAIService_pb2.BasicChatResponse(response=response_text)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    OpenAIService_pb2_grpc.add_OpenAIServiceServicer_to_server(Application(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
