from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    sudoku_board = [[0] * 9 for _ in range(9)]
    return render_template('base.html', sudoku_board=sudoku_board,sudoku_size=9)

@app.route('/update_cell', methods=['POST'])
def update_cell():
    global sudoku_board
    row = int(request.form['row'])
    col = int(request.form['col'])
    value = int(request.form['value'])

    # Update the Sudoku board with the entered value
    sudoku_board[row][col] = value

    # You can add additional logic for validation if needed

    return render_template('index.html', sudoku_board=sudoku_board,sudoku_size=9)

if __name__ == '__main__':
    app.run(debug=True)
