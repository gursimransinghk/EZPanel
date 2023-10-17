from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-fla', methods=['POST'])
def calculate_fla():
    data = request.json
    system_voltage = data['system_voltage']
    light_voltage = system_voltage / 1.732

    num_motors = data['num_motors']
    motor_flas = data['motor_flas']
    largest_motor_fla = max(motor_flas)
    adjusted_fla_motors = (largest_motor_fla * 1.25) + sum(motor_flas) - largest_motor_fla

    transformer_va = data['transformer_va']
    transformer_fla = transformer_va / system_voltage

    num_lights = data['num_lights']
    single_light_wattage = data['single_light_wattage']
    total_light_wattage = num_lights * single_light_wattage
    lighting_fla = total_light_wattage / light_voltage

    total_fla = adjusted_fla_motors + transformer_fla + lighting_fla

    return jsonify({"total_fla": round(total_fla, 2)})

if __name__ == '__main__':
    app.run(debug=True)
