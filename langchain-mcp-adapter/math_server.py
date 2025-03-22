from mcp.server.fastmcp import FastMCP
import logging

mcp = FastMCP("Math")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.getLogger().addHandler(console_handler)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    logger.info(f"Using add tool with {a} and {b}")
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    logger.info(f"Using multiply tool with {a} and {b}")
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")
