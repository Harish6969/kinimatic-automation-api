import json

def calculate_kinimatic_pricing(storage_needed, storage_type, number_of_regions):
    market_adjustment = 1.02
    base_cost = storage_needed * 0.50 * market_adjustment
    ecomm_multiplier = 1.05 if storage_type.lower() == "e-commerce" else 1.0
    adjusted_cost = base_cost * ecomm_multiplier
    region_cost = number_of_regions * 1000
    total_cost = adjusted_cost + region_cost
    total_cost = round(total_cost, 2)
    narrative = f"Base cost: ${base_cost:.2f} (market-adjusted). "
    if ecomm_multiplier > 1: narrative += f"E-commerce +5% = ${adjusted_cost:.2f}. "
    narrative += f"{number_of_regions} regions +${region_cost:.2f}. "
    narrative += f"Total: ${total_cost:.2f}."
    return total_cost, narrative

def handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        storage_needed = float(body.get('storage_needed', 0))
        storage_type = body.get('storage_type', '')
        number_of_regions = int(body.get('number_of_regions', 0))
        total_cost, narrative = calculate_kinimatic_pricing(storage_needed, storage_type, number_of_regions)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'total_cost': total_cost,
                'narrative': narrative,
                'sow': 'SOW placeholder',
                'rfp': 'RFP placeholder'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }