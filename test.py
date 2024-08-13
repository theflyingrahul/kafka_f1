from KafkaProducer import produce_message

produce_message('mercedes_distance', 'my-key', 'hamilton: 2.5s ahead')
produce_message('redbull_distance', 'my-key', 'pitstop requested')
