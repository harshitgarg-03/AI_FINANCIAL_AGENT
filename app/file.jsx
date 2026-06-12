const { useState } = require("react");


function greet() {
    const [Count, SetCount] = useState(1);
    return (
        <button
        onClick={() => {
            SetCount(Count+1)
        }}
        >
            {Count}
        </button>
    )
}

<greet/>