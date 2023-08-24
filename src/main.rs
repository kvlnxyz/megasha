fn add_binary(one: &str, two: &str, three: &str, four: &str) -> String {
    let mut value_int = 0;

    for x in 0..32 {
        let two: usize = 2;
        value_int += one.chars().nth(31-x) * two.pow(x);
    }

    // for x in 0..32 {
    //     value_int += two.chars().nth(31 - x).unwrap().to_digit(2).unwrap() * 2u32.pow(x as u128);
    // }

    // for x in 0..32 {
    //     value_int += three.chars().nth(31 - x).unwrap().to_digit(2).unwrap() * 2u32.pow(x as u128);
    // }

    // for x in 0..32 {
    //     value_int += four.chars().nth(31 - x).unwrap().to_digit(2).unwrap() * 2u32.pow(x as u128);
    // }

    value_int %= 2u32.pow(32);
    let value_binary = format!("{:032b}", value_int);

    value_binary
}

fn string_to_binary(input: &str) -> String {

    let mut binary_string: String = String::new();

    for c in input.chars() {
        let binary_repr = format!("{:08b}", c as u8);
        binary_string.push_str(&binary_repr);
    }

    binary_string.trim().to_string()

}

fn pad_message(input: String) -> String {
    let mut padded_message: String = String::new();

    padded_message += &input;

    padded_message += "1";

    let zero_count: usize = 448 - padded_message.len();
    let zeros: String = "0".repeat(zero_count);

    padded_message += &zeros;

    let binary_string = format!("{:b}", input.len());
    let more_zeros: String = "0".repeat(64 - binary_string.len());

    let l_add = more_zeros + &binary_string;

    padded_message += &l_add;

    padded_message

}

fn parse_message(input: String) -> Vec<String> {
    let mut word_blocks: Vec<String> = Vec::new();

    for x in 0..16 {
        if x * 32 + 32 <= input.len() {
            let slice: String = input[x * 32..x * 32 + 32].to_string();
            word_blocks.push(slice);
        }
    }

    word_blocks
}

fn rotate(binary: &str, amount: usize) -> String {
    let mut start = String::new();
    let mut end = String::new();

    let binary_len = binary.len();

    if binary_len >= amount {
        start = binary[binary_len - amount..].to_string();
        end = binary[..binary_len - amount].to_string();
    }

    return format!("{}{}", start, end);
}

fn shift(binary: &str, amount: usize) -> String {
    let start = "0".repeat(amount);
    let end = if binary.len() >= amount {
        binary[..binary.len() - amount].to_string()
    } else {
        String::from(binary)
    };

    return format!("{}{}", start, end);
}

fn sigma_zero(input: &str) -> String {
    let one = rotate(input, 7);
    let two = rotate(input, 18);
    let three = shift(input, 3);
    let mut output = String::new();
    for x in 0..32 {
        let addition = one.chars().nth(x).unwrap().to_digit(10).unwrap() +
                       two.chars().nth(x).unwrap().to_digit(10).unwrap() +
                       three.chars().nth(x).unwrap().to_digit(10).unwrap();
        output.push_str(&(addition % 2).to_string());
    }
    output
}

fn sigma_one(input: &str) -> String {
    let one = rotate(input, 17);
    let two = rotate(input, 19);
    let three = shift(input, 10);
    let mut output = String::new();
    for x in 0..32 {
        let addition = one.chars().nth(x).unwrap().to_digit(10).unwrap() +
                       two.chars().nth(x).unwrap().to_digit(10).unwrap() +
                       three.chars().nth(x).unwrap().to_digit(10).unwrap();
        output.push_str(&(addition % 2).to_string());
    }
    output
}

fn computation(input: Vec<String>) -> Vec<String> {
    let mut w: Vec<String> = input.clone();
    for x in 0..48 {
        let index: usize = x + 16;
        let one = sigma_one(&w[index - 2]);
        let two = &w[index - 7];
        let three = sigma_zero(&w[index - 15]);
        let four = &w[index - 16];
        let new_val = add_binary(&one, &two, &three, &four);
        w.push(new_val);
    }
    w
}



fn main() {
    let message: &str = "Testing function";
    let message_binary: String = string_to_binary(message);
    let padded_message: String = pad_message(message_binary);
    let padded_vec: Vec<String> = parse_message(padded_message);
    computation(padded_vec);
}

