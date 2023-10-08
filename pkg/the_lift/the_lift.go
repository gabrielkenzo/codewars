package thelift

const (
	up   Direction = "up"
	down Direction = "down"
)

type Direction string

type Lift struct {
	direction Direction
}

type People struct {
	queues []int
}

func TheLift(queues [][]int, capacity int) []int {
	direction := up
	floor := 0
	maxFloor := len(queues)
	path := []int{0}
	for true {
		if floor == 0 {
			direction = up
		}
		if floor == maxFloor {
			direction = down
		}

		if liftShouldStop() {
			peopleGetDown()
			peopleGetUp()

			path = append(path, floor)
		}

		if direction == "up" {
			floor += 1
		}
		if direction == "down" {
			floor -= 1
		}
	}
	return path
}

func liftShouldStop() bool {
	return true
}

func peopleGetDown() {

}
func peopleGetUp() {
}
