CC = gcc
CFLAGS = -O2 -Wextra -Wall
LDFLAGS = -lcrypto
TARGET = corrupted

all: $(TARGET)

$(TARGET): src/$(TARGET).c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

clean:
	rm -f $(TARGET)

package:
	bsdtar -cvaf $(TARGET).zip $(TARGET)

.PHONY: all clean package
