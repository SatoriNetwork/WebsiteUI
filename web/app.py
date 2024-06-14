#!/usr/bin/env python
# -*- coding: utf-8 -*-

import secrets
from waitress import serve
from flask import Flask, Response, render_template, jsonify, request, g, redirect

###############################################################################
## Globals ####################################################################
###############################################################################

debug = True
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
DEVMODE = True

###############################################################################
## Helpers ####################################################################
###############################################################################


def context(title: str = 'Satori', **kwargs):
    return {
        'title': title,
        **kwargs}

###############################################################################
## Errors #####################################################################
###############################################################################


@app.errorhandler(404)
def not_found(e):
    return '404', 404


###############################################################################
## Routes - Browser ###########################################################
###############################################################################


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/search/<term>', methods=['GET'])
def search(term=None):
    ''' searching for a stream '''
    try:
        return render_template(
            'home.html',
            **context(show='search', searchResults=[]))
    except Exception as e:
        return str(e), 400


@app.route('/vision', methods=['GET'])
def vision():
    ''' static data '''
    return render_template('home.html', **context(show='vision'))


@app.route('/roadmap', methods=['GET'])
def roadmap():
    ''' static data '''
    return render_template('home.html', **context(show='roadmap'))


@app.route('/team', methods=['GET'])
def team():
    ''' static data '''
    return render_template('home.html', **context(show='team'))


@app.route('/join', methods=['GET'])
def join():
    ''' static data '''
    return render_template('home.html', **context(show='join'))


@app.route('/download', methods=['GET'])
def download():
    ''' static data '''
    return render_template('home.html', **context(show='download'))


@app.route('/tokenomics', methods=['GET'])
def tokenomics():
    ''' static data '''
    # don't include it here because we just call it from js everytime anyway.
    # try:
    #    allocation = MintManifest.allocation()
    # except Exception as _:
    #    allocation = {
    #        'predictors': 0.5,
    #        'oracles': 0.2,
    #        'inviters': 0.05,
    #        'creators': 0.2,
    #        'managers': 0.05}
    return render_template('home.html', **context(
        show='tokenomics',
        # allocation=allocation
    ))


@app.route('/association/address', methods=['GET'])
def associationAddress():
    ''' evr account of association '''
    return jsonify({
        'address': 'https://rvn.cryptoscope.io/address/?address=RKj3w6vqfAopK3Ztwi91vUDEFdv71Qg3ti',
    }), 200


@app.route('/association/token', methods=['GET'])
def associationToken():
    ''' evr account of association '''
    return jsonify({
        'token': 'https://rvn.cryptoscope.io/asset/?asset_id=081cab6cd370fa387035b9fb5e67e736d7493453',
        'admin': 'https://rvn.cryptoscope.io/asset/?asset_id=b0615a9beb5ad1483f2fe4c8d5f546fce5e47fc0',
        'gensis': 'https://rvn.cryptoscope.io/tx/?txid=a015f44b866565c832022cab0dec94ce0b8e568dbe7c88dce179f9616f7db7e3'}), 200


###############################################################################
## Entry ######################################################################
###############################################################################


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5002,
        threaded=True,
        debug=debug,
        use_reloader=True)


# > python satori\web\app.py
