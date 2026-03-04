import threading
import time
from typing import Optional
"""
In-memory library
Key-value pair
TTL based auto-eviction
Persistence layer

FR
The KV library needs to be available to be imported
Caching will be having certain lifetime - N seconds
Precomputation when needed from DB to warm the cache
Extended


Assumption
Existing DB

NFR
Scale
1M in an hour -> 278 Write requests/ sec
Read is 1:5 -> 1400 read/ sec

Performance
SLO: Read and write both needs to be < 1 ms -> P95

API

GET v1/cache/{KEY}
{
id: 123,
Name: “abc”
TTL: 1000
}

POST
PUT
"""

class PersistentStorage:
    def __init__(self, input_file: "keyvaluepair.json"):
        self.input_file = input_file

    def load(self):
        pass
        # will come layer


class InMemoryPersistentStorage:
    def __init__(self, ttl: None):
        self.ttl = 1000
        self.store = {}
        self.lock = threading.Lock()
        self.thread = self._start_eviction_thread()

    def set(self, key: str, value: str, ttl: [Optional[int]] = None):
        ttl = ttl if ttl is not None else self.ttl
        with self.lock:
            self.store[key] = {"value": value, "expiry": ttl}
            self._persist(self.store)

    def get(self, key: str):
        pass

    def delete(self, key: str):
        with self.lock:
            if key in self.store:
                del self.store[key]
            self._persist(self.store)


    def _eviction_worker(self):
        while not self._stop_event().is_set():
            curr_time = time.time()

            with self.lock:
                keys_to_delete = [
                    key for key, value in self.store.items()
                    if value["expiry"] < curr_time
                ]

                for key in keys_to_delete:
                    del self.store[key]

                if keys_to_delete:
                    self._persist(self.store)


        def _start_eviction_thread(self):
            t = threading.Thread(target=self._eviction_worker, daemon=True)
            t.start()

    def shutdown(self):
        self._stop_event.set()



if __name__ == "__main__":
    persistence = InMemoryPersistentStorage()
    cache = InMemoryPersistentStorage(default_ttl = 1000, persistence = persistence)
    cache.set("a", 123)

    cache.shutdown()


