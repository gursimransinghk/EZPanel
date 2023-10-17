def control_panel_fla_calculator():
    # System Voltage
    system_voltage = float(input("Enter system voltage: "))
    
    # Determine single phase voltage for lights based on system voltage
    light_voltage = system_voltage / 1.732  # Assuming lights are connected to the same system

    # For Motors
    num_motors = int(input("Enter number of motors: "))

    if num_motors == 1:
        motor_flas = [float(input("Enter FLA for the motor: "))]
    else:
        same_fla = input("Do all motors have the same FLA? (yes/no): ").strip().lower()
        if same_fla == 'yes':
            common_fla = float(input("Enter the common FLA for all motors: "))
            motor_flas = [common_fla] * num_motors
        else:
            motor_flas = [float(input(f"Enter FLA for motor {i+1}: ")) for i in range(num_motors)]
    
    # Calculate FLA for motors
    largest_motor_fla = max(motor_flas)
    adjusted_fla_motors = (largest_motor_fla * 1.25) + sum(motor_flas) - largest_motor_fla

    # For Transformer
    transformer_va = float(input("Enter transformer VA rating: "))
    transformer_fla = transformer_va / system_voltage

    # For Lighting
    num_lights = int(input("Enter number of lights: "))
    single_light_wattage = float(input("Enter wattage for a single light: "))
    total_light_wattage = num_lights * single_light_wattage
    lighting_fla = total_light_wattage / light_voltage

    # Calculate total FLA
    total_fla = adjusted_fla_motors + transformer_fla + lighting_fla

    print(f"Total FLA for the control panel: {total_fla:.2f}A")

if __name__ == "__main__":
    control_panel_fla_calculator()
