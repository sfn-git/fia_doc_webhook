# CREATES -----------------------------------------------
CREATE_CONFIG_TABLE = """CREATE TABLE IF NOT EXISTS config(
    env TEXT, 
    skip_summary BOOLEAN,
    hash_only BOOLEAN,
    ollama_url TEXT,
    ollama_model TEXT,
    created_date DATE,
    updated_date DATE
    )"""
CREATE_WEBHOOKS_TABLE = """CREATE TABLE IF NOT EXISTS webhooks(
    wh_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    link TEXT,
    date_added DATE,
    date_updated DATE
)
"""
CREATE_DOCUMENTS_TABLE = """CREATE TABLE IF NOT EXISTS documents(
    doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    link TEXT,
    path TEXT,
    hash TEXT,
    document_date DATE,
    date_added DATE
)"""
CREATE_DOCUMENTS_SEND_TABLE = """CREATE TABLE IF NOT EXISTS document_send(
    send_id INTEGER PRIMARY KEY AUTOINCREMENT,
    wh_id INTEGER,
    doc_id INTEGER,
    sent BOOLEAN,
    skip BOOLEAN,
    date DATE,
    CONSTRAINT webhook_fk
        FOREIGN KEY (wh_id) REFERENCES webhooks (wh_id)
    CONSTRAINT docs_fk
    FOREIGN KEY (doc_id) REFERENCES documents (doc_id)
)"""
CREATE_DOC_SUMMARY_TABLE="""CREATE TABLE IF NOT EXISTS document_summary(
    summary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id INTEGER,
    prompt TEXT,
    summary TEXT,
    date DATE,
    ollama_url TEXT,
    ollama_model TEXT,
    CONSTRAINT docs_fk
    FOREIGN KEY (doc_id) REFERENCES documents (doc_id)

)"""
CREATE_SCHEDULE_TABLE="""CREATE TABLE IF NOT EXISTS schedule(
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_name TEXT,
    cron_timing TEXT,
    date_added DATE,
    date_updated DATE
)
"""
CREATE_DOCUMENT_TYPE_TABLE="""CREATE TABLE IF NOT EXISTS document_type(
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    keyword TEXT,
    active BOOLEAN,
    date_added DATE,
    date_updated DATE
)
"""
CREATE_PROMPT_TABLE="""CREATE TABLE IF NOT EXISTS prompts(
    prompt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    prompt TEXT,
    prompt_type TEXT CHECK(prompt_type IN ('SYSTEM', 'DOCTYPE', 'WEBHOOK', 'FUN')),
    link_id INTEGER,
    date_added DATE,
    date_updated DATE
)
"""

INSTRUCTION_PROMPT="""Do not greet when responding. Bold each header. Stay strictly to the format below."""

DEFAULT_SYSTEM_PROMPT ="""Race: [<Year> Name of Race]
Driver(s) Involved: [Only list the name of the Driver or car number if the name is not available]
Penalties/Allegation/Decision: [Bullet point driver that was punished and the penalties]
Summary: [Summarize the event that occurred in the document]""".lstrip().rstrip()

BASE_FIA_URL = "https://www.fia.com"