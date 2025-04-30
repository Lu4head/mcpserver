# Servidor MCP
Servidor Model Context Protocol para integração com Claude Desktop oferencendo um CRUD simples para que a LLM consiga interagir. MCP básico criado para aprendizado e estudo da tecnologia.

## Requisitos
- Python 3.10 ou superior
- uv
- bibliotecas necessárias listadas no arquivo `requirements.txt`

## Execução do programa
- Para executar o servidor, basta executar o arquivo `main.py`

## Configuração com Claude Desktop
- Para configurar o servidor com o Claude Desktop, basta adionar no arquivo `claude_desktop_config.json` a seguinte chave:
```json
{
    "mcpServers": {
        "mcp-test": {
            "command": "CAMINHO\\ABSOLUTO\\UV\\uv.exe",
            "args": [
                "--directory",
                "CAMINO\\ABSOLUTO\\REPOSITORIO\\mcpserver",
                "run",
                "main.py"
            ]
        }
    }
}
```