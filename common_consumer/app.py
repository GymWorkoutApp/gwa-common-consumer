from gwa_framework.schemas.pub_sub import PubSubMessage

from common_consumer.database import async_session
from common_consumer.models.goal import GoalModel
from common_consumer.pub_sub import consumer

if __name__ == '__main__':
    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))
        pub_sub_message = PubSubMessage(message.value)

        if pub_sub_message.operation == 'create':
            pub_sub_message.message
            goal = GoalModel
            with async_session() as session:
                session.add(goal)
                session.commit()




