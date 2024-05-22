from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from crud.activity import get_activities
from crud.factor import create_factor, get_factors
from crud.suplement import create_suplement, get_suplements
from crud.time import create_time
from schemas.process import ProcessCreate
from schemas.factor import CreateFactor
from schemas.time import CreateTime, CreateVeryTime

from crud.process import getProcess, create_process
from db.connection import SessinLocal
from schemas.suplement import CreateSuplement


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessinLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root(db: Session = Depends(get_db)):
    return getProcess(db)


@app.post('/createProcess')
async def createProcess(process: ProcessCreate, db: Session = Depends(get_db)):
    return create_process(db, process)

@app.get('/getActivities')
async def getActivities(db: Session = Depends(get_db)):
    return get_activities(db)

@app.get('/getFactors')
async def getFactors(db: Session = Depends(get_db)):
    return get_factors(db)

@app.post('/createFactor')
async def createFactor(factor: CreateFactor, db: Session = Depends(get_db)):
    return  create_factor(db, factor)

@app.get('/getSuplements')
async def getSuplements(db: Session = Depends(get_db)):
    return get_suplements(db)

@app.post('/createSuplement')
async def createSuplement(suplement: CreateSuplement, db: Session = Depends(get_db)):
    return create_suplement(db, suplement)

@app.post('/times')
async def time(time: CreateTime ,db: Session = Depends(get_db)):
    return create_time(db, time)

@app.post('/createListTimes')
async def createListTimes(times: CreateVeryTime ,db: Session = Depends(get_db)):
    times_list = []
    for time in times.tiempos:
        time = create_time(db, time)
        final_time = {
            'id' : time.id,
            'duracion' : time.duracion,
            'mano' : time.mano,
            'idActividad' : time.idActividad
        } 
        times_list.append(final_time)
    print(times_list)
    return times_list
