CC = gcc
CFLAGS = -O2 -Wextra -Wall
LDFLAGS = -lcrypto
TARGET = corrupted
SRC_DIR = src

all: $(TARGET)

victim: $(SRC_DIR)/$(TARGET).c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

$(TARGET): victim
	python $(SRC_DIR)/corrupt.py $< $@

clean:
	rm -f $(TARGET) victim $(TARGET).zip

package:
	rm victim
	bsdtar -caf $(TARGET).zip $(TARGET)

.PHONY: all clean package
