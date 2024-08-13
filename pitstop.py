from KafkaProducer import produce_message

def refuel(units):
    produce_message('redbull_pitstop', 'fuel', str(units))

def change_tyres(units):
    produce_message('mercedes_pitstop', 'tyre', str(units))
    
refuel(10)
change_tyres(4)