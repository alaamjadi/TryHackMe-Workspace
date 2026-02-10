#!/usr/bin/python3
import uuid
from datetime import datetime, timedelta, timezone

# UUID epoch: 15 October 1582 (RFC 4122)
UUID_EPOCH = datetime(1582, 10, 15, tzinfo=timezone.utc)

def uuid_v1_manual(dt, node, clock_seq):
    """
    Create a UUIDv1 for a specific datetime, node, and clock_seq.
    RFC 4122 compliant.
    """

    # timestamp in 100-nanosecond intervals
    timestamp = int((dt - UUID_EPOCH).total_seconds() * 1e7)

    time_low = timestamp & 0xffffffff
    time_mid = (timestamp >> 32) & 0xffff
    time_hi = (timestamp >> 48) & 0x0fff
    time_hi |= (1 << 12)  # version 1

    clock_seq_low = clock_seq & 0xff
    clock_seq_hi = (clock_seq >> 8) & 0x3f
    clock_seq_hi |= 0x80  # variant RFC 4122 (10xx xxxx)

    b = bytearray()
    b += time_low.to_bytes(4, "big")
    b += time_mid.to_bytes(2, "big")
    b += time_hi.to_bytes(2, "big")
    b.append(clock_seq_hi)
    b.append(clock_seq_low)
    b += node.to_bytes(6, "big")

    return uuid.UUID(bytes=bytes(b))


# ------------------------------------------------------------
# CONFIGURATION (edit this part)
# ------------------------------------------------------------

start_time = datetime(2025, 11, 20, 20, 0, tzinfo=timezone.utc)
end_time   = datetime(2025, 11, 20, 23, 59, tzinfo=timezone.utc)

# Fixed node from your dataset
node_hex = "026ccdf7d769"
node_int = int(node_hex, 16)

# A narrowed set of clock_seq candidates you extracted
clock_seq_list = [
    0xab3a, 0x96e7, 0x889c, 0x8acc, 0x93d8,
    0xac99, 0xbe28, 0xb7e8, 0xb231, 0xbb84, 0x8ad2
]

output_file = "generated_uuid_candidates.txt"

# ------------------------------------------------------------


print(f"Generating UUIDv1 values from {start_time} to {end_time} ...")

with open(output_file, "w") as f:
    dt = start_time
    while dt <= end_time:
        for cs in clock_seq_list:
            u = uuid_v1_manual(dt, node_int, cs)
            f.write(str(u) + "\n")
        dt += timedelta(minutes=1)

print(f"Done. UUID list saved to: {output_file}")
