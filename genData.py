import uuid
import struct


my_uuid = uuid.UUID('00000000-0000-0000-0000-000000000001')

data = struct.pack('>IHH8s', my_uuid.time_low, my_uuid.time_mid,
                   my_uuid.time_hi_version, my_uuid.bytes[8:])

name = "Hello world! How are you?"

data = data + struct.pack('>24s', name.encode('utf-8'))

birth_year = 2

data = data + struct.pack('>H', birth_year)

weight = 1.5

data = data + struct.pack('>d', weight)

rating = 5

data = data + struct.pack('>i', rating)

with open("build/animal_record.bin", "wb") as f:
    f.write(data)
