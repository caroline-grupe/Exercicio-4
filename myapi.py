#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:47:15 2023

@author: caroline
"""

from flask import Flask, jsonify
import json

app = Flask(__name__)

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def calcular_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    
def obter_dados_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados_json = json.load(file)
    return dados_json

@app.route('/calculos', methods=['POST'])
def calcular_resultados():
    try:
        dados_entrada = obter_dados_do_arquivo('data.txt')

        if 'fact' not in dados_entrada or 'fib' not in dados_entrada:
            return jsonify({'erro': 'As chaves "fact" e "fib" são obrigatórias.'}), 400

        fact = dados_entrada['fact']
        fib = dados_entrada['fib']

        resultado_fatorial = calcular_fatorial(fact)
        resultado_fibonacci = calcular_fibonacci(fib)

        resposta = {
            'fatorial': resultado_fatorial,
            'fibonacci': resultado_fibonacci
        }

        return jsonify(resposta)

    except Exception:
        return jsonify({'erro': 'Ocorreu um erro interno no servidor'}), 500


if __name__ == '__main__':
    app.run(debug=True)
