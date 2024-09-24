from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Carrega os dados anotados
variants_df = pd.read_csv('output/annotated_variants.csv')

@app.route('/variants', methods=['GET'])
def get_variants():
    frequency = request.args.get('frequency', type=float)
    dp = request.args.get('dp', type=int)

    # Simulação de filtro por DP
    filtered_variants = variants_df[(variants_df['FREQUENCY'] >= frequency)]

    return jsonify(filtered_variants.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
