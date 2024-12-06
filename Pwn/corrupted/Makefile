CC = gcc
CFLAGS = -O2 -Wextra -Wall
LDFLAGS = -lcrypto
TARGET = corrupted

all: $(TARGET)

victim: src/$(TARGET).c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

$(TARGET): victim
	python corrupt.py $< $@

clean:
	rm -f $(TARGET) victim $(TARGET).zip

package:
	rm victim
	bsdtar -caf $(TARGET).zip $(TARGET)

.PHONY: all clean package
