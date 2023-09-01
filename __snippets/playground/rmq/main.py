import pika

RABBITMQ_CONNECTION_STRING = "amqps://ulbqtwed:DyywqG8nzfd1J67xrBGHl0GJBYTKXyNw@sparrow.rmq.cloudamqp.com/ulbqtwed"
RABBITMQ_HOST = "sparrow.rmq.cloudamqp.com"
# RABBITMQ_HOST = "sparrow-01.rmq.cloudamqp.com"
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = "ulbqtwed"
RABBITMQ_PASSWORD = "DyywqG8nzfd1J67xrBGHl0GJBYTKXyNw"



def main():
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            virtual_host="ulbqtwed",
            credentials=credentials
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue="helloworld")
    channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!')
    channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!')
    channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
    # res1 = channel.get_waiting_message_count()
    # res2 = channel.basic_get(queue="helloworld")
    # print(res1)
    # print(res2)

if __name__ == "__main__":
    main()