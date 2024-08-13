from KafkaProducer import synchronous_produce_message

# synchronous_produce_message('mercedes_distance', 'my-key', 'hamilton: 2.5s ahead')
# synchronous_produce_message('redbull_distance', 'my-key', 'pitstop requested')
synchronous_produce_message('redbull_pitstop', 'my-key', 'at_pitstop')
synchronous_produce_message('redbull_fuel', 'my-key', '54.33%')
synchronous_produce_message('redbull_tyre', 'my-key', '54.33%')
