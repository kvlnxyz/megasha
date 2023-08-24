
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


fn main() {
    let message: &str = "Testing function";
    let message_binary: String = string_to_binary(message);
    let padded_message: String = pad_message(message_binary);
    let padded_vec: Vec<String> = parse_message(padded_message);

}

