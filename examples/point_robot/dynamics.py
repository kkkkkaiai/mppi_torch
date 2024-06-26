import torch


class OmnidirectionalPointRobotDynamics:
    def __init__(self, dt=0.05, device="cuda:0") -> None:
        self._dt = dt
        self._device = device

    def step(self, states: torch.Tensor, actions: torch.Tensor, t: int) -> torch.Tensor:
        x, y, theta = states[:, 0], states[:, 1], states[:, 2]

        new_x = x + actions[:, 0] * self._dt
        new_y = y + actions[:, 1] * self._dt
        new_theta = theta + actions[:, 2] * self._dt

        new_states = torch.stack([new_x, new_y, new_theta], dim=1)
        return new_states, actions
