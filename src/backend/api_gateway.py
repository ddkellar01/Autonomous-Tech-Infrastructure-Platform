from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from src.core.engine import MasterOrchestrator

app = FastAPI(title="Autonomous Tech Engine API", version="1.0.0")
orchestrator = MasterOrchestrator()

class ScoutRequest(BaseModel):
    orgs: list[str] = ["google", "microsoft", "apache"]

@app.post("/api/v1/scout")
async def trigger_scout(req: ScoutRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(orchestrator.run_autonomous_cycle, req.orgs)
    return {"status": "Accepted", "message": "Autonomous scout cycle initiated in background."}

@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy", "service": "autonomous-engine-api"}
