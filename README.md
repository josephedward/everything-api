# Everything API

The Everything API is a thought experiment and learning exercise that explores the potential of OpenAI's GPT model to generate web content dynamically based on URL paths. The concept is simple: any path entered into the URL becomes a query that is sent to the GPT model, which then generates the content for the resulting page on the fly.

## How It Works

When a request is made to a certain path, that path is treated as a prompt for the GPT model. The model then generates a page of content based on that prompt, which means every page is unique and is generated dynamically based on the user's query.

For instance, a navigation to `/actors/steve_buscemi` will yield a GPT-generated page about Brad Pitt, while `/recipes/chocolate_chip_cookies` will prompt the API to create a page about making chocolate chip cookies.

## Setup

To experiment with the Everything API, ensure you have Node.js installed and follow these steps:

1. Clone the repository: git clone https://github.com/josephedward/everything-api-flask-vercel
2. Navigate into the directory: cd everything-api
3. Install dependencies: pip install -r requirements.txt
4. Create a .env file with your OpenAI API key: echo "OPENAI_API_KEY=your_key_here" > .env
5. Deploy your application on Vercel:
    - Install Vercel CLI if you haven't already: npm i -g vercel
    - Link your project to an existing project on Vercel: vercel link
    - Deploy your project: vercel

**Note:** Make sure your Python version and all necessary environment variables are properly configured in the Vercel settings for your project. The command vercel link will guide you through the process of linking your local project to Vercel. It's necessary to have a Vercel account and a project already set up.

You can now navigate to `localhost:3000` and begin exploring the Everything API!

## Limitations and Considerations

While the Everything API demonstrates the potential of GPT models, it's important to acknowledge the limitations. The quality and relevance of generated content is reliant on the GPT model, which, although powerful, isn't flawless. The response time can vary based on the size of the prompt and the number of tokens requested, potentially impacting user experience.

## Origin

The Everything API is an open project, and contributions are welcome! If you have a feature request, bug report, or proposal, feel free to open an issue on our GitHub repository. If you're interested in contributing code, please open a pull request.

## Contributing

This project is primarily a learning exercise and was inspired by this [tutorial video](https://www.youtube.com/watch?v=M2uH6HnodlM) from LiveUnderflow. It aims to demonstrate the power and potential of GPT models in creating highly dynamic and flexible web applications.

## License

The Everything API is an open source project, licensed under the MIT license. Please refer to the `LICENSE` file for more information.

<!-- ## Flask + Vercel
This example shows how to use Flask 2 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python). -->
<!-- 
## How it Works
This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions. -->
