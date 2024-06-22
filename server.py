import asyncio

import websockets

from ChatDialog import ChatDialog


async def websocket_handler(websocket: websockets.WebSocketServerProtocol, path: str) -> None:
    if path != "/chat":
        await websocket.close()
        return
    try:
        # 客户端连接
        chat = ChatDialog()
        await websocket.send(chat.hello_message)

        async for message in websocket:
            # 接收到消息
            response = chat.process_message(message)
            await websocket.send(response)

    except websockets.exceptions.ConnectionClosedError:
        # 断开连接
        print(f"Connection closed by client {websocket.remote_address}")


async def main():
    host = "localhost"
    port = 8765

    async with websockets.serve(websocket_handler, host, port):
        print(f"WebSocket server started at ws://{host}:{port}")
        await asyncio.Future()  # 永远不会完成的 Future，保持服务器运行


if __name__ == "__main__":
    asyncio.run(main())
