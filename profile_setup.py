import jinja2
from IPython.lib import passwd


if __name__=='__main__':
    data={}
    r = raw_input("Make remotely accessible? (y/N): ")
    if r.lower() == 'y':
        data['remoteaccess'] = True
    else:
        data['remoteaccess'] = False
    if data['remoteaccess']:
        data['password'] = passwd()
    with open("ipython_notebook_config.py.tmpl") as f:
        t = jinja2.Template(f.read())
    with open(".ipython/profile_nbserver/ipython_notebook_config.py", "wb") as f:
        f.write(t.render(**data))
