#version 330 core

const int NUM_LIGHT_SRC = 4;

const float density = 0.007;
const float gradient = 1.5;

uniform mat4 projection, view, model;
uniform vec3 light_position[NUM_LIGHT_SRC];

const int MAX_VERTEX_BONES=4, MAX_BONES=128;
uniform mat4 bone_matrix[MAX_BONES];

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 uvs;
layout(location = 2) in vec3 normal;
layout(location = 3) in vec4 bone_ids;
layout(location = 4) in vec4 bone_weights;

out vec3 fragment_color;
out vec2 frag_uv;
out vec3 to_light_vector[NUM_LIGHT_SRC];

out vec3 w_position, w_normal;
out float visibility;

void main() {

    vec4 worldPosition = model * vec4(position, 1.0);
    vec4 positionRelativeToCam = view * worldPosition;

    mat4 skin_matrix = mat4(0);
    for (int b=0;b< MAX_VERTEX_BONES;b++)
        skin_matrix += bone_weights[b] * bone_matrix[int(bone_ids[b])];

    vec4 w_position4 = skin_matrix * vec4(position, 1.0);
    
    gl_Position = projection * view * w_position4;
    frag_uv = vec2(uvs.x,1-uvs.y);

    w_position = w_position4.xyz / w_position4.w;

    w_normal = transpose(inverse(mat3(model))) * normal;

    for(int i = 0;i < NUM_LIGHT_SRC; i++)
    {
        to_light_vector[i] = light_position[i] - worldPosition.xyz;
    }

    float distance = length(positionRelativeToCam.xyz);
    visibility = exp(-pow((distance * density), gradient));
    visibility = clamp(visibility, 0.0, 1.0);

}
