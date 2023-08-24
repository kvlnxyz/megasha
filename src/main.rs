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

fn main() {
    let message: &str = "RedBlockBlue";
    let message_binary: String = string_to_binary(message);
    let padded_message = pad_message(message_binary);
    println!("{}", padded_message);

    // println!("Message is {}", message);
}

