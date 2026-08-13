
def is_manual_run(context):
    dag_run = context.get('dag_run')
    conf = dag_run.conf or {}
    return conf.get('manual_run',False)
def is_dry_run(context):
    dag_run = context.get('dag_run')
    conf = dag_run.conf or {}
    return conf.get('dry_run',False)

def setting_eviroment():
    print("SETUP: loading all enviroment variables and settings...")

def cleaning_enviroment():
    print("TEARDOWN: cleaning enviroment variables and temp files...")

def compliance_audit():
    print("COMPLIANCE: running deep dive verification against production records...")

def data_to_warehouse():
    print("WAREHOUSE: Successfully streaming sanitized updates to database records...")