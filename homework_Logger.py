import asyncio
import aiofiles
from datetime import datetime
from enum import Enum
import os

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"

class AsyncLogger:
    def __init__(self, filename=None):
        self.filename = filename or f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    async def _write_log(self, level: LogLevel, message: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level.value}] {message}\n"
        
        async with aiofiles.open(self.filename, mode='a') as f:
            await f.write(log_entry)

    async def debug(self, message: str):
        await self._write_log(LogLevel.DEBUG, message)

    async def info(self, message: str):
        await self._write_log(LogLevel.INFO, message)

    async def error(self, message: str):
        await self._write_log(LogLevel.ERROR, message)

class AsyncTaskQueue:
    def __init__(self, logger: AsyncLogger):
        self.queue = asyncio.Queue()
        self.logger = logger

    async def add_task(self, task_data):
        await self.queue.put(task_data)
        await self.logger.info(f"Task added: {task_data}. Queue size: {self.queue.qsize()}")

    async def process_task(self):
        if self.queue.empty():
            await self.logger.debug("Queue is empty, waiting for tasks...")
            return None

        task = await self.queue.get()
        await self.logger.info(f"Processing task: {task}. Remaining: {self.queue.qsize()}")
        
        # Имитация обработки задачи
        await asyncio.sleep(1)
        
        self.queue.task_done()
        return task

    async def shutdown(self):
        if not self.queue.empty():
            await self.logger.error("Shutting down with tasks still in queue!")
        else:
            await self.logger.info("Graceful shutdown - queue is empty")
        return self.queue.empty()

async def main():
    logger = AsyncLogger()
    task_queue = AsyncTaskQueue(logger)

    await logger.info("Starting application")
    
    # Добавляем задачи
    for i in range(1, 4):
        await task_queue.add_task(f"Task_{i}")

    # Обрабатываем задачи
    while not task_queue.queue.empty():
        await task_queue.process_task()

    # Завершаем работу
    await task_queue.shutdown()
    await logger.info("Application finished")

if __name__ == "__main__":
    asyncio.run(main())