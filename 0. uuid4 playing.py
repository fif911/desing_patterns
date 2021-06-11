import uuid
import time

start_time = time.time()
i = 0
# В 100 раз быстрее!!!
# UUIDs generated: 4 331 747 in 120.00062775611877 s
# UUIDs generated: 4 332 308 in 120.00362753868103 s
while True:
    new_uuid = uuid.uuid4()
    i += 1
    print(f"UUIDs generated: {i} in {time.time() - start_time} s")

# UUIDs generated: 43 055 in 120.00382137298584 s
# while True:
#     new_uuid = uuid.uuid4()
#     print(f"UUIDs generated: {len(uuid_list)} in {time.time() - start_time} s")
#     if new_uuid in uuid_list:
#         print(f"new uuid is in uuid_list !!!!!\n"
#               f"{new_uuid}")
#         break
#
#     uuid_list.append(new_uuid)
