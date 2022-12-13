from time import perf_counter
from fastapi import Request


class RequestTimingMiddleware:
    async def __call__(self, request: Request, call_next):
        start_time = perf_counter()
        # process the request and get the response    
        response = await call_next(request)
        process_time = perf_counter() - start_time
        response.headers["X-Process-Time"] = f'{process_time:0.4f} sec'
        return response
