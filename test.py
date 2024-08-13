from KafkaProducer import synchronous_produce_message

# synchronous_produce_message('mercedes_distance', 'my-key', 'hamilton: 2.5s ahead')
# synchronous_produce_message('redbull_distance', 'my-key', 'pitstop requested')
synchronous_produce_message('redbull_pitstop', 'my-key', '30 40')

