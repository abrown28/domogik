from domogik.admin.application import app, render_template, timeit
from flask import request, flash, redirect
from domogikmq.reqrep.client import MQSyncReq
from domogikmq.message import MQMessage
from flask_login import login_required
try:
    from flask_babel import gettext, ngettext
except ImportError:
    from flask.ext.babel import gettext, ngettext
    pass

@app.route('/upgrade')
@login_required
@timeit
def upgrade():
    with app.db.session_scope():
        devs = app.db.list_devices(d_state=u'upgrade')
    
    return render_template('upgrade.html',
        mactive="upgrade",
        devices=devs
        )

@app.route('/upgrade/<int:devid>')
@login_required
@timeit
def upgrade_dev(devid):
    return render_template('upgrade_input.html',
        mactive="upgrade"
        )
