from invoke import task

@task
def start(ctx):
	ctx.run("python3 main.py", pty=True)
	