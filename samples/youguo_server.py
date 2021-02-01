import sys
import os
import traceback
from typing import Dict
import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.responses import FileResponse
from samples.example_youguo import get_acos_enc, get_acos_dec

app = FastAPI()
app.debug = True

from typing import Dict
from fastapi import FastAPI
from starlette.status import HTTP_200_OK
from pydantic import Field
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    args: str = Field(...)


class ResultData(BaseModel):
    content: str


async def resp_encode_200(*, status_code: int, code: int = 0, data: Union[Dict, str],
                          message: str = "success") -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "data": data,
            "code": code,
            "message": message
        }
    )


async def resp_decode_200(*, status_code: int, code: int = 0, data: Union[Dict, dict],
                          message: str = "success") -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "data": data,
            "code": code,
            "message": message
        }
    )


@app.post("/encryption")
async def encryption(data: Data):
    data: bytearray = get_acos_enc(enc_string=data.args)
    return await resp_encode_200(status_code=HTTP_200_OK, data=str(data))



@app.post("/decryption")
async def encryption(resultdata: ResultData):
    return_data: dict = get_acos_dec(enc=resultdata.content)
    return await resp_decode_200(status_code=HTTP_200_OK, data=return_data)


if __name__ == '__main__':
    # command = "uvicorn youguo_server:app --host 0.0.0.0 --port 7881 --reload"
    # os.system(command)
    # uvicorn.run(app='youguo_server:app', host="192.168.1.125", port=7881, reload=True, debug=True)
    uvicorn.run(app='youguo_server:app', host="0.0.0.0", port=7881, reload=True, debug=True)

