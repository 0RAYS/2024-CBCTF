CC = gcc
CFLAGS  = -Wextra -Wall -O2 -fpie -fstack-protector
ASFLAGS = -Wextra -Wall -O2 -fpie
LDFLAGS = -z now -pie -z noexecstack
TARGET 	= StackLogout

SRC_DIR = src
BUILD_DIR = build
SRC = main.c who.s

SRCS = $(patsubst %,$(SRC_DIR)/%,$(SRC) $(SRC))
OBJS = $(patsubst %.c,$(BUILD_DIR)/%.o,$(filter %.c,$(SRC))) $(patsubst %.s,$(BUILD_DIR)/%.o,$(filter %.s,$(SRC)))

ifdef DEBUG
	CFLAGS  += -g
	ASFLAGS += -g
endif

all: $(BUILD_DIR) $(TARGET)

$(BUILD_DIR):
	mkdir -p $@

src/who-ref.s: src/who.c
	$(CC) -S $(CFLAGS) -o $@ $<

reference: src/who-ref.s

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.s
	$(CC) -c $(ASFLAGS) -o $@ $<
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) -c $(CFLAGS) -o $@ $<

$(TARGET): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^

clean:
	rm -f $(OBJS) $(TARGET)

print:
	@echo $(OBJS) $(SRCS)
.PHONY: all clean reference print
