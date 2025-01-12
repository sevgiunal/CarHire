from livereload import Server
from render_all_lite import render_all

if __name__ == "__main__":
    # Initial render on startup
    render_all()

    # Set up the livereload server
    server = Server()

    # Watch for changes in the templates/ and data/ directories
    server.watch("templates/**/*.jinja", render_all)
    server.watch("templates/**/*.html", render_all)
    server.watch("data/*.json", render_all)
    server.watch("data/*.[yY][aA][mM][lL]", render_all)
    server.watch("style/*.css", render_all)

    # Serve the generated site
    server.serve(root="site", port=5519)
