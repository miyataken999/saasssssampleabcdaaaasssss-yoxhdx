import logging
from converter.vmware_converter import VMwareConverter
from models.sakura_server_config import SakuraServerConfig
from utils.logger import setup_logger

def main():
    setup_logger()
    logging.info("Starting Sakura Server to VMware Converter")
    
    # Load Sakura Server configuration
    sakura_config = SakuraServerConfig()
    
    # Create VMware Converter instance
    converter = VMwareConverter(sakura_config)
    
    # Perform conversion
    converter.convert()

if __name__ == "__main__":
    main()