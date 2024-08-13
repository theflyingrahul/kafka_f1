from KafkaProducer import synchronous_produce_message

def refuel(units):
    synchronous_produce_message('redbull_pitstop', 'fuel', str(units))

def change_tyres(units):
    synchronous_produce_message('mercedes_pitstop', 'tyre', str(units))
    
refuel(10)
change_tyres(4)