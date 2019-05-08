DEFINES+=PROJECT_CONF_H=\"project-conf.h\"

CONTIKI_TARGET_SOURCEFILES += adc-sensors.c dht22.c

all: mqtt-exmaple

APPS += mqtt

# Linker size optimization
SMALL = 1

CONTIKI_WITH_IPV6 = 1

CONTIKI = ../../../..

include $(CONTIKI)/Makefile.include
