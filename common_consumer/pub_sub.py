import pickle

from kafka import KafkaConsumer

from common_consumer.settings import GWA_ENVIRONMENT
from common_consumer.settings import GWA_KEY
from common_consumer.settings import PubSubSettings

consumer = KafkaConsumer(*PubSubSettings.TOPICS.values(),
                         bootstrap_servers=f'{PubSubSettings.HOST}:{PubSubSettings.PORT}',
                         client_id=f'{GWA_ENVIRONMENT}-{GWA_KEY}',
                         group_id=PubSubSettings.GROUP_ID,
                         value_deserializer=lambda m: pickle.loads(m),
                         key_deserializer=lambda m: pickle.loads(m),
                         api_version=(0, 10))
