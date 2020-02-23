from src.consumer.consumer import ConsumersManager

if __name__ == '__main__':
    manager = ConsumersManager()
    manager.set_consumers()
    manager.start_consumers()
