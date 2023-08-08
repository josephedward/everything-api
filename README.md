# Everything API

The Everything API is a thought experiment and learning exercise that explores the potential of OpenAI's GPT model to generate web content dynamically based on URL paths. The concept is simple: any path entered into the URL becomes a query that is sent to the GPT model, which then generates the content for the resulting page on the fly.

This project is primarily a learning exercise and was inspired by this [tutorial video](https://www.youtube.com/watch?v=M2uH6HnodlM) from LiveUnderflow. It aims to demonstrate the power and potential of GPT models in creating highly dynamic and flexible web applications.


## How It Works

When a request is made to a certain path, that path is treated as a prompt for the GPT model. The model then generates a page of content based on that prompt, which means every page is unique and is generated dynamically based on the user's query.

For instance, a navigation to `/actors/steve_buscemi` will yield a GPT-generated page about Stephen Buscemi, while `/recipes/chocolate_chip_cookies` will prompt the API to create a page about making chocolate chip cookies.

## Setup

To experiment with the Everything API, ensure you have Node.js installed and follow these steps:

1. Clone the repository: git clone https://github.com/josephedward/everything-api-flask
2. Navigate into the directory: cd everything-api
3. Install dependencies: pip install -r requirements.txt
4. Create a .env file with your OpenAI API key: echo "OPENAI_API_KEY=your_key_here" > .env
5. Check Render's Flask demo project (https://render.com/docs/deploy-flask)


## Limitations and Considerations

While the Everything API demonstrates the potential of GPT models, it's important to acknowledge the limitations. The quality and relevance of generated content is reliant on the GPT model, which, although powerful, isn't flawless. The response time can vary based on the size of the prompt and the number of tokens requested, potentially impacting user experience.


## License

The Everything API is an open source project, licensed under the MIT license. Please refer to the `LICENSE` file for more information.
